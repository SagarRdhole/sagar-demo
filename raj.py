apiVersion: apps/v1
kind: Deployment
metadata: 
  name: fusion-labs-frontend
spec: 
  replicas: 5
  selector: 
    matchLabels: 
      tier: fusion-labs-frontend
  template:
    metadata:  
      labels: 
        tier: fusion-labs-frontend
    spec: 
      containers: 
       - name: nginx-service
         image: nginx