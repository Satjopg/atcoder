import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int f = sc.nextInt();
		int s = sc.nextInt();
		System.out.println(f * s % 2  == 1 ? "Odd" : "Even");
	}
}