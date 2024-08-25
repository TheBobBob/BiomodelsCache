
import {searchModels, getModel} from "../src/searchClient/getBiomodels.js" // location of search client

const lookUpBtn = document.getElementById("lookUpInfoBtn");
const searchText = document.getElementById("search_words");

window.onload = function() {
	lookUpBtn.addEventListener("click", (_) => lookUpModelInfo());
	
}

async function lookUpModelInfo() {
	const searchTerms = searchText.value;
	const searchResults = await searchModels(searchTerms); // ***** <-- Here is the Call ******** 
	
	let recommendMap = searchResults.models;
	let modelResultsStr = "";
	for (const rec of recommendMap) {
		const modelId = rec[0] // Only two elements of rec, first holds model id, 2nd holds array of key-value pairs
		console.log(modelId);
		modelResultsStr = modelResultsStr + modelId + ": \n";
		const modelInfo = rec[1]
		modelResultsStr = modelResultsStr + JSON.stringify(modelInfo) + " \n";
	}
		
	const modelTextArea = document.getElementById("model_info"); 
	modelTextArea.value = modelResultsStr;
	
	getBioModel("BIOMD0000000002")  // <-- hard coded
}

async function getBioModel(modelID) {
	const model_text = await getModel(modelID); //  <-- getModel Call ***************
	const model_strTextArea = document.getElementById("model_text")
	model_strTextArea.value = model_text;
	
	
}