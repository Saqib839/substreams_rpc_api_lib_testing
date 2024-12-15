import ctypes

# Load the Rust shared library
lib = ctypes.CDLL('./libreqstreams.so')  # Update the path as needed

# Define the argument and return types for the FFI function
lib.api_call_ffi.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.api_call_ffi.restype = ctypes.c_char_p

# Define the free_string function
lib.free_string.argtypes = [ctypes.c_char_p]
lib.free_string.restype = None

# Test the function
api_url = b"https://httpbin.org/get"
# optional_headers = b'{"User-Agent": "Rust-Client"}'  # Optional headers as JSON
optional_headers = b'{}'

# result_ptr = lib.api_call_ffi(api_url, optional_headers)
result_ptr = lib.api_call_ffi(api_url, optional_headers)

# Convert the result to a Python string and free the memory
result = ctypes.c_char_p(result_ptr).value.decode()
# lib.free_string(result_ptr)

print(f"API Call Result: {result}")
