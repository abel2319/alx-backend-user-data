#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":

    try:
        from api.v1.auth.session_auth import SessionAuth
        sa = SessionAuth()
        user_id_1 = "User 1"
        session_id_1 = sa.create_session(user_id_1)
        if session_id_1 is None:
            print("Can't create session ID")
            exit(1)
        print(session_id_1)
        new_user_id_1 = sa.user_id_for_session_id(session_id_1)
        if new_user_id_1 is None:
            print("user_id_for_session_id doesn't return the user ID linked to the session ID")
            exit(1)
        
        if new_user_id_1 != user_id_1:
            print("user_id_for_session_id doesn't return the user ID linked to the session ID created previously")
            exit(1)
        
        print("OK", end="")
    except:
        import sys
        print("Error: {}".format(sys.exc_info()))
