use reqstreams::run_substream;
use reqstreams::rpc_call;
use reqstreams::api_call;
use anyhow::Error;
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Error> {

// Uncomment for testing substreams

    // let endpoint_url = "https://mainnet.eth.streamingfast.io:443".to_string();
    // let package_file = "https://github.com/streamingfast/substreams-uniswap-v3/releases/download/v0.2.10/substreams-uniswap-v3-v0.2.10.spkg";
    // let module_name = "uni_v0_2_9:map_pools_created";
    // let block_range = Some("21133036:21333938".to_string());

    // let results = run_substream(endpoint_url, package_file, module_name, block_range).await?;

    // for decoded_data in results {
    //     println!("{:?}\n\n", decoded_data); // Output each decoded data
    // }

// Uncomment for testing rpc_call

    // Example usage of the rpc_call function
    let rpc_endpoint = "https://mainnet.infura.io/v3/e2df7af7a38e41d9a7334ce930e566c9";
    let method = "eth_getBalance";
    let params_input = "[\"0x3843889b7356e89e63581A594ad826B1F1C445f5\", \"latest\"]";
    let id = 1;

    match rpc_call(rpc_endpoint, method, params_input, id).await {
        Ok(response) => {
            println!("Response: {}", serde_json::to_string_pretty(&response)?);
        }
        Err(err) => {
            eprintln!("Error: {:?}", err);
        }
    }

// Uncomment for testing api_call

//     // Example usage of the api_call function
//     let api_url = "https://httpbin.org/get";
//     let optional_headers = Some("{\"Authorization\": \"Bearer token\"}");

//     match api_call(api_url, optional_headers).await {
//         Ok(response) => {
//             println!("API Response: {}", response);
//         }
//         Err(err) => {
//             eprintln!("API Error: {:?}", err);
//         }
//     }

    Ok(())
}