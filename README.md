# 🧰 Ten Utils Library

![Python](https://img.shields.io/badge/python-3.13-blue)  
![License](https://img.shields.io/badge/license-MIT-green)  
![PyPI Version](https://img.shields.io/pypi/v/ten-utils)  
![Downloads](https://img.shields.io/pypi/dm/ten-utils)

Welcome to **Ten Utils**, a lightweight Python utility library designed to simplify common development tasks with robust logging, environment variable management, and more! 🚀

---

## Features ✨

### 1. Logger

- Structured and stylized logging with **colored console output**.
    
- Five logging levels:
    
    - `DEBUG` (0) 🐞
        
    - `INFO` (1) ℹ️
        
    - `WARNING` (2) ⚠️
        
    - `ERROR` (3) ❌
        
    - `CRITICAL` (4) 🔥
        
- Global log level threshold control.
    
- Optionally include **caller information** and **timestamps**.
    
- Designed for **future file logging support**.
    

Example:

```python
from ten_utils.log import Logger

logger = Logger(name="MyModule")
logger.info("This is an info message")
logger.error("Something went wrong")
```

### 2. EnvLoader 🌱

- Load environment variables from `.env` files or directly from system environment.
    
- Automatic type casting: `str`, `int`, `float`, `bool`, `list`, `tuple`, `dict`.
    
- Validates values and raises meaningful errors if missing or invalid.
    

Example:

```python
from ten_utils.env_loader import EnvLoader

loader = EnvLoader(path_to_env_file=".env")
db_host = loader.load("DB_HOST", str)
port = loader.load("DB_PORT", int)
```

### 3. Buffer 🧰

- Singleton-based **in-memory key-value storage**.
    
- Useful for caching or temporary storage within your application.
    

Example:

```python
from ten_utils.buffer import Buffer

buffer = Buffer()
buffer.set("user", "Alice")
print(buffer.get("user"))  # Output: Alice
buffer.clear()  # Clear all cached values
```

### 4. Singleton Pattern 🔒

- Simple metaclass to create singleton classes.
    
- Ensures only one instance exists.
    
- Can clear instances if needed.
    

Example:

```python
from ten_utils.singleton import Singleton

class MyClass(metaclass=Singleton):
    pass

instance1 = MyClass()
instance2 = MyClass()
assert instance1 is instance2  # True
```

### 5. Custom Errors ❗

- Base exception class: `TenUtilsLibError`
    
- EnvLoader specific errors:
    
    - `FailedLoadEnvVariables`
        
    - `FailedConvertTypeEnvVar`
        
    - `NotFoundNameEnvVar`
        

Example:

```python
from ten_utils import EnvLoader, FailedLoadEnvVariables

try:
    loader = EnvLoader("invalid.env")
except FailedLoadEnvVariables as e:
    print(e)
```

---

## Installation 💾

```bash
pip install ten-utils
```

---

## Quick Start ⚡

```python
from ten_utils import Logger, EnvLoader, Buffer

# Logger example
logger = Logger(name="App")
logger.debug("Debug message")
logger.info("Info message")

# EnvLoader example
loader = EnvLoader(".env")
db_url = loader.load("DB_URL", str)

# Buffer example
buffer = Buffer()
buffer.set("token", "abc123")
print(buffer.get("token"))
```

---

## Contributing 🤝

We welcome contributions! Please follow these steps:

1. Fork the repository.
    
2. Create a new branch.
    
3. Make your changes.
    
4. Submit a pull request.
    

---

## License 📝

This project is licensed under the **MIT License**.