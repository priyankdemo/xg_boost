# importing the requests library
import requests
# defining the api-endpoint
API_ENDPOINT = "http://115.115.91.60:5432/train"
# data to be sent to api
data = {
	"url": "https://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@github.com/MJ410/classify-private",
	"branch_name": "main",
	"user_name": "jay@gmail.com"
}
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)