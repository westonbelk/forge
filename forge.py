#!/usr/bin/env python3
import argparse
import subprocess



def main(env, playbook):
	extra_arguments = "@{0!s}".format(env)

	subprocess.run( \
		[
			"ansible-playbook", playbook,
			"--become", "--ask-become-pass",
		 	"-e", extra_arguments
		], \
		shell=False, check=False)



if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("-e", "--environment", help="environment template to create", required=True)
	parser.add_argument("-p", "--playbook", help="the ansible playbook to run", required=True)
	parser.add_argument("--id", help="environment identification number")

	args = parser.parse_args()
	main(args.environment, args.playbook)