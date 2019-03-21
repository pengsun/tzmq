A toy example that shows how to run actor-learner dist RL with k8s.

## Separate Run
As usual, each job (role) can be run separately, e.g.,
```bash
python learner.py --port 9999

python actor.py --lrn_addr learner-name:9999 --task_index 0

python actor.py --lrn_addr learner-name:9999 --task_index 1

python actor.py --lrn_addr learner-name:9999 --task_index 55
```
will start 1 learner and 3 actors,
where the `learner-name` can be either an IP or a domain name (provided the DNS service is available in your intra-net).

## k8s
Starting the jobs one by one manually is tedious. 
Surely we can write a dedicated frontend script to start all jobs.
But a better choice is to rely on some cluster management tool, e.g., 
the Kubernetes (k8s).
This way, we can do 
"Alright, I need 1 learner over GPU machine, 
3 actors over CPU machines, that's it. 
I don't care (want to manage) the ip address or domain name."

### docker
First, pack as docker image:
```bash
docker build --tag my_tzmq:latest .
```
which generates an image named `tzmq`. 
You can verify it by the `docker images` command.

Use `docker attach` to get in and do any modification,
and use `docker commit` to save the changes and update the image.
Or you can redo the `docker build` (should be reasonably fast as many intermediate files are reused internally)

### k8s start and stop
Start it with k8s:
```bash
python render_template.py tzmq.template.jinja | kubectl create -f -
```
Note: `kubectl create -f` means creating from file,
the second single dash `-` indicates a special file the `stdin`,
and finally the pipe operator `|` forwards the output string.

Stop it:
```bash
python render_template.py tzmq.template.jinja | kubectl delete -f -
```

### logs
Use `kubectl get pods` to show pod names,
and use `kubectl logs pod_id` to show the log (stdout) of that container.

TODO: describe more elaborated tool (Grafana, etc.)

## notes
### Related Methods
Two ways to run distributed RL/ML over k8s: 
the template based way as in [dist tf ecosystem]( https://github.com/tensorflow/ecosystem) and `kubeflow` based way. 
Here we show the template based way, which is light-weight.

### job/role name
k8s has internal DNS service, use `kubectl get svc -n kube-system` to verify it.
Therefore, we can use the domain name (instead of IP address) in the `tzmq.template.jinja` template.
