from google.protobuf.message import DecodeError
from typing import Callable, Dict, Any
from pb.uniswap.v1 import uniswap_pb2  # Adjust the import as per your generated protobuf files

# Define a type alias for decoder functions
DecoderFn = Callable[[bytes], Any]

# Decoding functions

def decode_pools(data: bytes):
    """Decode data into Pools message."""
    decoded = uniswap_pb2.Pools()
    decoded.ParseFromString(data)
    return decoded

def decode_erc20_tokens(data: bytes):
    """Decode data into ERC20Tokens message."""
    decoded = uniswap_pb2.ERC20Tokens()
    decoded.ParseFromString(data)
    return decoded


# Module-to-decoder mapping
MODULES: Dict[str, DecoderFn] = {
    "map_pools_created": decode_pools,
    "uni_v0_2_9:map_pools_created": decode_pools,
    # "graph_out": decode_entity_changes,
    # "uni_v0_2_9:graph_out": decode_entity_changes,
    "uni_v0_2_9:map_tokens_whitelist_pools": decode_erc20_tokens,
    # Add more mappings here
}

def decode_with_module(module_name: str, data: bytes) -> Any:
    """Decode data using the appropriate decoder function based on the module name."""
    decoder = MODULES.get(module_name)
    if decoder is None:
        raise ValueError(f"No decoder registered for module: {module_name}")
    try:
        return decoder(data)
    except DecodeError as e:
        raise ValueError(f"Failed to decode data for module '{module_name}': {e}")
