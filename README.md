A toy example that shows to run actor-learner dist RL with k8s.

Two ways: template based as in [dist tf ecosystem]( https://github.com/tensorflow/ecosystem) or `kubeflow` based. 
We show the template based way, which is light-weight.

## Separate Run
```bash
python learner.py --port 9999

python actor.py --lrn_addr localhost:9999 --task_index 0

python actor.py --lrn_addr localhost:9999 --task_index 1

python actor.py --lrn_addr localhost:9999 --task_index 55
```

## k8s
First, pack as docker image:
```bash
docker build tzmq .
```

Then, run it with k8s:
```bash
python render_template.py tzmq.template.jinja | kubectl create -f -
```
Note: `kubectl create -f` means creating from file,
the second single dash `-` indicates a special file the `stdin`,
and finally the pipe operator `|` forwards the output string.
