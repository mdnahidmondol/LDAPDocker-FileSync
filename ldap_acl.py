import ldap
import os
import pwd
import grp

def get_ldap_user_info(username, ldap_server, base_dn):
    conn = ldap.initialize(ldap_server)
    conn.protocol_version = ldap.VERSION3
    
    search_filter = f"(uid={username})"
    attributes = ['uidNumber', 'gidNumber']
    
    result = conn.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter, attributes)
    
    if result:
        return result[0][1]
    return None

def set_file_permissions(filepath, uid, gid):
    os.chown(filepath, uid, gid)
    os.chmod(filepath, 0o770)  # rwxrwx---

def sync_permissions(directory, ldap_server, base_dn):
    for root, dirs, files in os.walk(directory):
        for item in dirs + files:
            filepath = os.path.join(root, item)
            username = os.path.basename(os.path.dirname(filepath))
            
            user_info = get_ldap_user_info(username, ldap_server, base_dn)
            if user_info:
                uid = int(user_info['uidNumber'][0])
                gid = int(user_info['gidNumber'][0])
                set_file_permissions(filepath, uid, gid)

if __name__ == "__main__":
    sync_permissions('/data', 'ldap://ldap_server:389', 'dc=example,dc=com')