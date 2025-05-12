from fastapi import FastAPI, Depends # type: ignore
from typing import Annotated

app = FastAPI()

# Dependency function
def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

# Route using the dependency
@app.get("/get-simple-goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    return response



from fastapi import FastAPI, Depends, Query
from typing import Annotated

app = FastAPI()

# Dependency function with parameter
def get_goal(username: str = Query(...)):  # ... means it's required
    return {"goal": "We are building AI Agents Workforce", "username": username}

# Route
@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response


from fastapi import FastAPI, Depends, Query
from typing import Annotated

app = FastAPI()

# Dependency function for login check
def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}

# Route using the dependency
@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    return user


from fastapi import FastAPI, Depends, Query
from typing import Annotated

app = FastAPI()

# Dependency 1 - Goal
def dep_goal():
    return {"goal": "We are building AI Agents Workforce"}

# Dependency 2 - Login
def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}

# Route with both dependencies
@app.get("/mission")
def mission_api(
    goal: Annotated[dict, Depends(dep_goal)],
    user: Annotated[dict, Depends(dep_login)]
):
    return {"goal": goal, "login_status": user}


from fastapi import FastAPI, Depends, Query
from typing import Annotated

app = FastAPI()

# Class-based Dependency
class LoginForm:
    def __init__(self, username: str = Query(None), password: str = Query(None)):
        self.username = username
        self.password = password

    def is_valid(self):
        return self.username == "admin" and self.password == "admin"

# Route
@app.get("/check")
def check_login(form: Annotated[LoginForm, Depends()]):
    if form.is_valid():
        return {"message": "Welcome, admin!"}
    else:
        return {"message": "Invalid credentials"}


from fastapi import FastAPI, Depends, Query
from typing import Annotated

app = FastAPI()

# Class-based Dependency
class LoginForm:
    def __init__(self, username: str = Query(None), password: str = Query(None)):
        self.username = username
        self.password = password

    def is_valid(self):
        return self.username == "admin" and self.password == "admin"

# External function that takes dependency
def validate_user(form: Annotated[LoginForm, Depends()]):
    if not form.is_valid():
        raise ValueError("Invalid user")
    return form

# Route
@app.get("/secure-data")
def get_secure_data(user: Annotated[LoginForm, Depends(validate_user)]):
    return {"message": f"Secure content for {user.username}"}
