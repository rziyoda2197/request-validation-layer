from pydantic import BaseModel, validator
from typing import Optional

class Request(BaseModel):
    name: str
    age: int
    email: Optional[str]

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Name must not be empty')
        return v

    @validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be a positive integer')
        return v

    @validator('email')
    def email_must_be_valid(cls, v):
        if v and not v.count('@') == 1:
            raise ValueError('Invalid email format')
        return v

def validate_request(request: Request):
    try:
        request.validate()
        return True
    except ValueError as e:
        return False

# Misol:
request = Request(name='John Doe', age=30, email='john@example.com')
if validate_request(request):
    print('Request is valid')
else:
    print('Request is invalid')
```

```python
from pydantic import BaseModel, validator
from typing import Optional

class Request(BaseModel):
    name: str
    age: int
    email: Optional[str]

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Name must not be empty')
        return v

    @validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be a positive integer')
        return v

    @validator('email')
    def email_must_be_valid(cls, v):
        if v and not v.count('@') == 1:
            raise ValueError('Invalid email format')
        return v

def validate_request(request: Request):
    try:
        request.validate()
        return True
    except ValueError as e:
        return False

# Misol:
request = Request(name='John Doe', age=30, email='john@example.com')
if validate_request(request):
    print('Request is valid')
else:
    print('Request is invalid')
