//138747-20161205-22d78a0c

public class day1 {
	public static void main(String[] args) {
		String directions = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2";
		String[] list = directions.split(", ");
		int dir = 0;
		int posx = 0;
		int posy = 0;
		for (int i = 0; i < directions.length()-1; i++) {
			if (list[i].substring(0,1).equals("R"))
				dir++;
			else if (list[i].substring(0,1).equals("L"))
				dir--;

			int move = Integer.parseInt(list[i].substring(1));
			System.out.println(move);
			System.out.println(dir);
			if (dir%4 == 0)
				posy += move;
			else if ((dir%4 == 1) || (dir == -3) || (dir == -7))
				posx += move;
			else if ((dir%4 == 2) || (dir == -2) || (dir = -6))
				posy -= move;
			else if ((dir%4 == 3) || (dir == -1) || (dir = -5))
				posx -= move;
			System.out.println(posx +","+posy);
		}
		System.out.println(posx + posy);
	}

}