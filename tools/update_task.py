import requests

# To issue a put request via requests
# resp = requests.put("URL", json=mydata)

URL = "http://127.0.0.1:5000/tasks/2"

def update_task_by_id(summary, description):
    new_task = {
        "summary": summary,
        "description": description
    }
    response = requests.put(URL,json=new_task)
    if response.status_code == 204:
        print("Task successfully created!")
    else:
        print("Something went wrong while trying to update task.")

if __name__ == "__main__":
    update_task_by_id("Test my service", "Validate that the record is updated")