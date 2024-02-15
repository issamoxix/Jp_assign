from .forms import LegalRequestForm, DocumentAttachmentForm
from .models import LegalRequest
from django.http import JsonResponse
from rest_framework.views import APIView
from datetime import datetime
from .permissions import IsAuthenticatedCookie

class SubmitLegalRequestView(APIView):
        
    def post(self, request):
        legal_request_form = LegalRequestForm(request.POST)
        document_attachment_form = DocumentAttachmentForm(request.POST, request.FILES)

        if legal_request_form.is_valid() and document_attachment_form.is_valid():
            client = legal_request_form.save()
            legal_request = LegalRequest(
                client=client,
                case_description=legal_request_form.cleaned_data["case_description"],
                case_type=legal_request_form.cleaned_data["case_type"],
                status="open"
            )
            legal_request.save()

            document = document_attachment_form.save(commit=False)
            document_name = document.document.name.split('.')
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            document.document.name = f'{document_name[0]}_{timestamp}.{document_name[1]}'  # Append timestamp to the file name
            document.legal_request = legal_request
            document.save()

            return JsonResponse(status=201, data={"message": "Legal request submitted successfully"})
        
        return JsonResponse(status=400, data={"message": "Invalid data"})

    def get(self, request):
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))
        
        legal_requests = LegalRequest.objects.all().values()
        total = max(legal_requests.count(), 10)
        legal_requests = legal_requests[offset:offset+limit]
        return JsonResponse(data={"legal_requests": list(legal_requests), "pages": total // 10, "offset": offset, "limit": limit})

class LegalRequestView(APIView):
    permission_classes = [IsAuthenticatedCookie]

    def get(self, request, id):
        legal_request = LegalRequest.objects.filter(id=id).values()
        return JsonResponse(data={"legal_request": list(legal_request)})
    
    def put(self, request, id):
        legal_request = LegalRequest.objects.filter(id=id).first()
        legal_request.status = request.data["status"]
        legal_request.save()
        return JsonResponse(data={"message": "Legal request updated successfully"})