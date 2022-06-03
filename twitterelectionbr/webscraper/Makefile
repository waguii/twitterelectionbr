#------------GCLOUD-------------
# project id - replace with your GCP project id
PROJECT_ID=twiiter-effect-in-elections

# bucket name - replace with your GCP bucket name
BUCKET_NAME=twiiter-effect-in-elections-bucket

# choose your region from https://cloud.google.com/storage/docs/locations#available_locations
REGION=europe-west1

# path to the file to upload to GCP (the path to the file should be absolute or should match the directory where the make command is ran)
# replace with your local path to the `train_1k.csv` and make sure to put the path between quotes
LOCAL_PATH="raw_data/aecio.csv"


set_project:
	@gcloud config set project ${PROJECT_ID}

create_bucket:
	@gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}

upload_data:
	@gsutil cp ${LOCAL_PATH} gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${BUCKET_FILE_NAME}
