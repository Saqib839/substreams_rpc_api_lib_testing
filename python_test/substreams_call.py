import ctypes

# Load the Rust shared library
lib = ctypes.CDLL('/mnt/c/Users/MuhammadSaqib/Documents/substreams_rust_sdk/target/release/libreqstreams.so')  # Update the path as needed

# Define the argument and return types for the FFI function
lib.run_substream_ffi.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
lib.run_substream_ffi.restype = ctypes.c_char_p

# Define the free_string function
lib.free_string.argtypes = [ctypes.c_char_p]
lib.free_string.restype = None

# Test the function
endpoint_url = b"mainnet.eth.streamingfast.io:443"
package_file = b"https://github.com/streamingfast/substreams-uniswap-v3/releases/download/v0.2.10/substreams-uniswap-v3-v0.2.10.spkg"  # Example package file path
module_name = b"uni_v0_2_9:map_tokens_whitelist_pools"
range = b"21331100:21335101"
# range = b""

result_ptr = lib.run_substream_ffi(endpoint_url, package_file, module_name, range)

# Convert the result to a Python string and free the memory
result = ctypes.c_char_p(result_ptr).value.decode()
# lib.free_string(result_ptr)

print(f"\n{result}")
