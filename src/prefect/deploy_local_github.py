"""
Note: this K8s manifest requires a Prefect Cloud workspace, for OSS K8s deployment, consider https://github.com/PrefectHQ/prefect-helm
prefect kubernetes manifest agent --work-queue default --image-tag prefecthq/prefect:2-python3.9 --namespace default | kubectl apply --namespace=default -f -
"""
from prefect.infrastructure import Process

from dataplatform.deploy_utils import build_image, save_block, bash
import flows.entrypoints_config as cfg

deploy_agent = True
image_agent = "prefecthq/prefect:2-python3.9"
k8s_namespace = "prefect"
image_name = "dataplatform"
block_name = "default"
name = "k8s"
queue_and_blocks_name = "default"
ib = f"-ib process/{queue_and_blocks_name}"
build = "prefect deployment build"
queue_name = "k8s"
wq = f"-q {queue_name}"
sb = f"-sb github/random-git"


if __name__ == "__main__":
    #bash("python utilities/create_blocks.py")
    # process_block = Process(env={"PREFECT_LOGGING_LEVEL": "DEBUG"})
    # save_block(process_block, queue_and_blocks_name)

    # Deploy FLOWS
    bash(f"{build} {ib} {sb} {wq} -n {name} {cfg.maintenance_flow} -a")

    for flow in cfg.main_flows:
        tags = "-t parent"
        bash(f"{build} {ib} {sb} {wq} {flow} {tags} -n {name} -a")
