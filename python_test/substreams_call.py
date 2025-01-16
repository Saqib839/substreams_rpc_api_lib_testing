import ctypes
from ctypes import c_char_p, c_void_p, c_size_t, POINTER, Structure
import pb.uniswap.v1.uniswap_pb2 as uniswap_pb2;
from module_map import decode_with_module 

# Define the FfiByteArray structure in Python to match the Rust definition
class FfiByteArray(Structure):
    _fields_ = [("data", ctypes.POINTER(ctypes.c_uint8)), 
                ("length", ctypes.c_size_t)]

# Load the compiled shared library
lib = ctypes.CDLL("/mnt/c/Users/MuhammadSaqib/Documents/substreams_rpc_api_lib_testing/lib/libunifiedstreams.so")  # Replace with your .dll on Windows

# Define the `substreams_call_ffi` function prototype
lib.substreams_call_ffi.argtypes = [
    c_char_p,  # endpoint_url
    c_char_p,  # package_file
    c_char_p,  # module_name
    c_char_p,  # range
    POINTER(c_size_t),  # out_length
]
lib.substreams_call_ffi.restype = POINTER(FfiByteArray)

# Define the `free_byte_array` function prototype
lib.free_byte_array.argtypes = [POINTER(FfiByteArray), c_size_t]
lib.free_byte_array.restype = None

# Input parameters
endpoint_url = b"mainnet.eth.streamingfast.io:443"
package_file = b"https://github.com/streamingfast/substreams-uniswap-v3/releases/download/v0.2.10/substreams-uniswap-v3-v0.2.10.spkg"  # Example package file path
module_name = "uni_v0_2_9:map_tokens_whitelist_pools"
byte_module_name = module_name.encode("utf-8")
range = b"21335037:21335538"

# Output length placeholder
out_length = c_size_t(0)

# Call the FFI function
results_ptr = lib.substreams_call_ffi(endpoint_url, package_file, byte_module_name, range, ctypes.byref(out_length))

# Process the results
if results_ptr:
    print(f"Received {out_length.value} results:")
    results = ctypes.cast(results_ptr, POINTER(FfiByteArray * out_length.value)).contents

    for i, result in enumerate(results):
        # Access the byte array data
        data = ctypes.string_at(result.data, result.length)
        print(f"\nResult {i + 1}: {data}")
        
        # print("\nDecoded Protobuf message:")
        try:
            # Dynamically decode the Protobuf data using the module_map
            decoded_message = decode_with_module(module_name, data)
            print(decoded_message)
        except ValueError as e:
            print(f"Decoding error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
else:
    print("Error: substreams_call_ffi returned null.")
