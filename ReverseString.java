class ReverseString{
    public static void main(String[] args){
        String givenString = "Sarah tommy";
        reverseWord(givenString);
    }
    
    public static void reverseWord(String words){
        helper(0, words);
    }
    public static void helper(int index, String word){
        if(index==word.length() || word==null){
            return;
        }
        helper(index+1, word);
        System.out.print(word.charAt(index));
    }
}