import time
from fastapi import FastAPI
from helper import process_json_file
from worker_task import analyse_tweet

app = FastAPI(name="tweet_audit")

@app.post("/start_audit")
async def start_audit(criteria: dict):
	audit_job_id = "AUDIT-" + str(int(time.time()))
	task_ids = []
	filename = "large_tweet_archive_50MB.json"
	JSON_PREFIX = "item"
	for tweet in process_json_file(filename, JSON_PREFIX):
		result = analyse_tweet.delay(tweet, criteria, audit_job_id)
		task_ids.append(result.id)
		
		return {"status": "Job queuer successfully",  "job_id": audit_job_id, "task_count": len(task_ids)}
