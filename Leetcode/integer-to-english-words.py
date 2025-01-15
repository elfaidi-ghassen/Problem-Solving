class Solution {
public:

string numberToWordsHelper(int n) {
	if (n <= 0) return "";
	else if (n <= 19) {
		switch (n % 100) {
		case 1: return "One";
		case 2: return "Two";
		case 3: return "Three";
		case 4: return "Four";
		case 5: return "Five";
		case 6: return "Six";
		case 7: return "Seven";
		case 8: return "Eight";
		case 9: return "Nine";
		case 10: return "Ten";
		case 11: return "Eleven";
		case 12: return "Twelve";
		case 13: return "Thirteen";
		case 14: return "Fourteen";
		case 15: return "Fifteen";
		case 16: return "Sixteen";
		case 17: return "Seventeen";
		case 18: return "Eighteen";
		case 19: return "Nineteen";
		}
	}
	else if (n < 1E2) {
		string tens;
		switch (n % 100 / 10) {
		case 2: tens = "Twenty"; break;
		case 3: tens = "Thirty"; break;
		case 4: tens = "Forty"; break;
		case 5: tens = "Fifty"; break;
		case 6: tens = "Sixty"; break;
		case 7: tens = "Seventy"; break;
		case 8: tens = "Eighty"; break;
		case 9: tens = "Ninety"; break;
		}
		if (n % 10 == 0)
			return tens;
		else
			return tens + ' ' + numberToWordsHelper(n % 10);
	}
	else if (n < 1E3) {
		int hundreds = n / 100; 
		string result = numberToWordsHelper(hundreds) + " Hundred";
		if (n % 100 == 0)
			return result;
		else return result + ' ' + numberToWordsHelper(n % 100);
	}
	else if (n < 1E6) {
		int thousand = n / 1000;
		string result = numberToWordsHelper(thousand) + " Thousand";
		if (n % 1000 == 0)
			return result;
		else return result + ' ' + numberToWordsHelper(n % 1000);
	}
	else if (n < 1E9) {
		int million = n / 1000000;
		string result = numberToWordsHelper(million) + " Million";
		if (n % 1000000 == 0)
			return result;
		else return result + ' ' + numberToWordsHelper(n % 1000000);
	}
	else {
		int million = n / 1000000000;
		string result = numberToWordsHelper(million) + " Billion";
		if (n % 1000000000 == 0)
			return result;
		else return result + ' ' + numberToWordsHelper(n % 1000000000);
	}
	return "";
}

string numberToWords(int n) {
    if (n == 0) {
        return  "Zero";
    }
    else return numberToWordsHelper(n);
}



};
