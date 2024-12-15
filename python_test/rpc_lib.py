import ctypes

# Load the Rust shared library
lib = ctypes.CDLL('./libreqstreams.so')  # Update the path as needed

# Define the argument and return types for the FFI function
lib.rpc_call_ffi.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
lib.rpc_call_ffi.restype = ctypes.c_char_p

# Define the free_string function
lib.free_string.argtypes = [ctypes.c_char_p]
lib.free_string.restype = None

# Test the function
rpc_endpoint = b"https://mainnet.infura.io/v3/e2df7af7a38e41d9a7334ce930e566c9"
method = b"eth_getBalance"
params = b'["0x3843889b7356e89e63581A594ad826B1F1C445f5", "latest"]'
id = 1

result_ptr = lib.rpc_call_ffi(rpc_endpoint, method, params, id)

# Convert the result to a Python string and free the memory
result = ctypes.c_char_p(result_ptr).value.decode()
# print(f"Result pointer: {result_ptr}")
# lib.free_string(result_ptr)

print(f"RPC Call Result: {result}")

