import ldap
import os

def authenticate_ldap(username, password):
    ldap_server = os.environ.get('LDAP_SERVER', 'ldap://ldap_server:389')
    base_dn = os.environ.get('LDAP_BASE_DN', 'dc=example,dc=com')
    
    try:
        conn = ldap.initialize(ldap_server)
        conn.protocol_version = ldap.VERSION3
        conn.simple_bind_s(f"uid={username},{base_dn}", password)
        return True
    except ldap.INVALID_CREDENTIALS:
        return False
    except ldap.LDAPError as e:
        print(f"LDAP error: {e}")
        return False
    finally:
        conn.unbind_s()

# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    if authenticate_ldap(username, password):
        print("Authentication successful")
    else:
        print("Authentication failed")
