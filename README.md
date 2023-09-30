# deployment commands

## deployment command (grc) (can be called for one of the methods)
gcloud builds submit --tag gcr.io/{projectid}/{method-name-to-use-when-calling}
gcloud run deploy --image gcr.io/{projectid}/{method-name-to-use-when-calling} --platform managed