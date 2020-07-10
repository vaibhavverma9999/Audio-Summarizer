	//Prepare form data
function lol()
{
	var input = document.querySelector('input[type=file]'),
	file = input.files[0];
	var formData = new FormData();
	formData.append("file", file);
	formData.append("language"   , "eng");
	formData.append("apikey"  , "06a4e7c02088957");
	//Send OCR Parsing request asynchronously
	jQuery.ajax({
	url: 'https://api.ocr.space/parse/image',
	data: formData,
	dataType: 'json',
	cache: false,
	contentType: false,
	processData: false,
	type: 'POST',
	success: function (ocrParsedResult) {
	//Get the parsed results, exit code and error message and details
	//console.log("success");
	var parsedResults = ocrParsedResult["ParsedResults"];
	var ocrExitCode = ocrParsedResult["OCRExitCode"];
	var isErroredOnProcessing = ocrParsedResult["IsErroredOnProcessing"];
	var errorMessage = ocrParsedResult["ErrorMessage"];
	var errorDetails = ocrParsedResult["ErrorDetails"];
	var processingTimeInMilliseconds = ocrParsedResult["ProcessingTimeInMilliseconds"];
	//If we have got parsed results, then loop over the results to do something
	if (parsedResults!= null) {
	//Loop through the parsed results
	$.each(parsedResults, function (index, value) {
	var exitCode = value["FileParseExitCode"];
	var parsedText = value["ParsedText"];
	var errorMessage = value["ParsedTextFileName"];
	var errorDetails = value["ErrorDetails"];
	var textOverlay = value["TextOverlay"];
	var pageText = '';
	console.log(parsedText);
	var ocr = document.getElementById("ocr-results");
	var results = document.getElementById("results");
	var save = document.getElementById("ocr-save");
	ocr.innerHTML = parsedText;
	results.style.display = results.style.display == "none" ? "block" : "none";
	ocr.style.display = ocr.style.display == "none" ? "block" : "none";
});
}
}
});
}