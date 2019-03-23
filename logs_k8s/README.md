Solution to log collection and viewing.
The officially recommended logging architecture is described [here](https://kubernetes.io/docs/concepts/cluster-administration/logging/).
Basically, we need:
* A log sampler (e.g., `fluentd`) on each Node/Pod
* A log text searching service (e.g., `elasticsearch`)
* A visualization/viewing tool (e.g., `kibana` or `grafana`)

A concrete solution is the `EFK` (`Elasticsearch` + `Fluentd` + `Kibana`) as described [here](https://kubernetes.io/docs/tasks/debug-application-cluster/logging-elasticsearch-kibana/).
We take a similar solution adopted from the [Aliyun doc](https://www.alibabacloud.com/help/zh/doc-detail/68264.htm),
where all the docker images are Aliyun urls and `Fluentd` is replaced with `log-pilot`.

## Install all
First, execute the following three commands sequentially:
```bash
kubectl apply -f elasticsearch.yml
kubectl apply -f log-pilot.yml
kubectl apply -f kibana.yml
```
Use `kubectl get`, `kubectl describe` and `kubectl logs` to make sure all Pods/Services have been successfully started.

## How to use
Edit `tzmq.template.jinja` to make sure the `log_stdout` variable is set.
Start the actor-learner task as usual:
```bash
python render_template.py ../tzmq.template.jinja | kubectl create -f -
```

Now, you can view the collected logs through `kibana` in a web browser, where:
* the port can be found by `kubectl get svc kibana_svc_name` 
* `Kibana -> Management -> Index name or pattern` should be set to `tzmq` (see the `tzmq.template.jinja` `env` field)

[A snapshot](tzmq_kibana.png)