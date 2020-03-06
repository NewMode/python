from newmode import Newmode

api = Newmode()

payload = {
	"first_name": "Mark",
	"last_name": "Styles",
	"email_address": "lambic@pm.me",
	"postal_code": "H4E 2Y7",
	"email_subject": "This is my subject",
	"your_letter": "This is my letter"
}

print(api.getOutreach(37))