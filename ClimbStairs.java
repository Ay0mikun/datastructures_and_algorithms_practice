import java.util.*;

class ClimbStairs{
    private static HashMap<Integer, Integer> lookup = new HashMap<Integer, Integer>();
    private static int climbStairs(int num) {
        if(num <= 2){
            lookup.put(num, num);
            return num;
        }
        if(lookup.containsKey(num)){
            return lookup.get(num);
        }
        lookup.put(num , climbStairs(num - 1) + climbStairs(num - 2));
        return lookup.get(num);
    }

    public static void main(String[] args){
        System.out.println("Climb stairs for "+climbStairs(6));
    }
}