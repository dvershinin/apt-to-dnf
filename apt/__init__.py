import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument('-y', action='store_true') # or --yes or  --assume-yes, while --force-yes or -y
    # TODO map that to "--assumeyes" in `yum`
    # args, unknown = parser.parse_known_args(['--foo', 'BAR', 'spam'])
    args, unknown = parser.parse_known_args()
    print(args)
    # Namespace(foo='BAR')
    cli_cmd = ["dnf"]
    # if args.y:
    #     cli_cmd = cli_cmd + ["-y"]
    cli_cmd = cli_cmd + unknown
    print("Running: " + " ".join(cli_cmd))
    subprocess.run(cli_cmd)