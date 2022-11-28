# How to deplot this Flask API (GCP)

1. Create Project
2. Go to Cloud Run
3. Activate cloud shell (right top)
4. Clone git repo to google cloud

```
git clone https://github.com/Blue-Cheesecake/Gin-Gun.git
cd Gin-Gun
cd server
```

5. Open Editor

- move Dockerfile, pyenv.cfg, and requirements.txt to app folder

6. Click `Cloud Code` on bottom left
7. Test on Cloud Emulator to see if it's work
8. Deploy on Cloud run

- Specify Service Name
- Select where server is

9. Go to cloud run dashboard
10. Select new running instance
11. Click edit & deploy new revision
12. Go to connectors
13. Create custom connector
