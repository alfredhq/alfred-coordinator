import argparse
import yaml
import zmq


def get_config(path):
    with open(path) as file:
        return yaml.load(file)


def run(config):
    context = zmq.Context()

    frontend = context.socket(zmq.PULL)
    frontend.bind(config['frontend'])

    backend = context.socket(zmq.PUSH)
    backend.bind(config['backend'])

    try:
        zmq.device(zmq.STREAMER, frontend, backend)
    finally:
        frontend.close()
        backend.close()
        context.term()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('config')

    args = parser.parse_args()
    config = get_config(args.config)

    run(config)


if __name__ == '__main__':
    main()
