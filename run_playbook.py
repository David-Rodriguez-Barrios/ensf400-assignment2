import ansible_runner

import os
run_configuration = ansible_runner.RunnerConfig(
    private_data_dir='./',
    playbook='./hello.yml',
    envvars={'ANSIBLE_CONFIG': './ansible.cfg'}
)

run_configuration.prepare()
ansible_runner.run_command('docker compose up -d')
run = ansible_runner.Runner(config=run_configuration)
run.run()

print("-"*20)
print("Testing Round Robin curl to 0.0.0.0:")
for i in range(8):
    print(os.popen("curl --silent http://0.0.0.0").read())
