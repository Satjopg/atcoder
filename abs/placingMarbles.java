import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String f = sc.next();
		int c = 0;
		if ("000".equals(f)) {
			c = 0;
		} else if ("111".equals(f)) {
			c = 3;
		} else {
			for (String s : f.split("")) {
				if ("1".equals(s)) c++;
			}
		}
		System.out.println(c);
	}
}