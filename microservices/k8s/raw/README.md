# Kubernetes artificat

Below are the way to generate required artificats

   kubectl create serviceaccount inventory --dry-run -o yaml > serviceaccount.yml 
   kubectl run inventory --image inventory --serviceaccount=inventory --dry-run -o yaml > deployment.yml
   kubectl expose deployment inventory --type=NodePort --port=80 --target-port=8000 --dry-run -o yaml > service.yml 

