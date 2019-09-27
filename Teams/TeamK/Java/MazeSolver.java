import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;



public class MazeSolver {
	
	static int startCol;
	static int startRow;
	static int endCol;
	static int endRow;
	static int dim;
	
	
	static String empty ="0";
	static String obstacle = "1";
	static String start = "2";
	static String target = "3";
	static String [][] parts;
	public static Queue<Node> queue = new LinkedList<Node>();
	
	
	public static void loadMaze() {
		BufferedReader br = null;
		
		try {
			br = new BufferedReader(new FileReader(new File("C:\\Users\\Kora\\Desktop\\Kora\\Privat\\Furtwangen\\CodeCamp\\MazeRunner\\MazeExamples\\maze1.txt")));
//			String line = br.readLine();
			
			String readLine;
			int num =0;
			while ((readLine = br.readLine()) != null) {
				
				String[] ch =readLine.split(",");
				if(num==0) {
				 dim = ch.length;
				 parts = new String[dim][dim];
				}
				for(int i=0; i< ch.length; i++) {
					parts[num][i] =ch[i];
				}
				num++;
					
					}

		System.out.print("Given maze: ");
		for(int i=0; i<parts.length; i++) {
			System.out.println();
			for(int j=0; j<parts.length;j++) {
				System.out.print(parts[i][j]+ " ");
			}
		}
		System.out.println();
		System.out.println();

		} catch(FileNotFoundException e) {
			e.printStackTrace();
		} catch(IOException e) {
			e.printStackTrace();
		} finally {
			if(br != null) {
				try {
					br.close();
				} catch(IOException e) {
					e.printStackTrace();
				}
			}
		}
}
	
	public static void setStart() {
		for(int i=0; i<parts.length; i++) {
			for(int j=0; j<parts.length; j++) {
				if(parts[i][j].equals(start)) {
					startCol=i;
					startRow=j;
				}
			}
		}
		System.out.println("Start:"+startCol + ":"+ startRow);
	}
	
	
	public static void setEnd() {
		for(int i=0; i<parts.length; i++) {
			for(int j=0; j<parts.length; j++) {
				if(parts[i][j].equals(target)) {
					endCol=i;
					endRow=j;
				}
			}
		}
		System.out.println("Ende:"+endCol + ":"+ endRow);
		System.out.println();
		System.out.println();
	}
	
	public static class Node{
		int x;
		int y;
		Node parent;
		
		
		 public Node(int x, int y, Node parent) {
	            this.x = x;
	            this.y = y;
	            this.parent = parent;
	        }

	        public Node getParent() {
	            return this.parent;
	        }

	        public String toString() {
	            return "x = " + x + " y = " + y;
	        }
	}
	
	
	
	public boolean removeNode(Node n) {
		return false;
	}
	
	public static Node solveMaze(int x, int y) {
		
		System.out.print("Looking for Exit! ");
		
		queue.add(new Node(x,y,null));
		
		while(!queue.isEmpty()) {
			System.out.print(".");

			Node n = queue.remove();
			
			if (parts[n.x][n.y].equals(target)) {
				System.out.println("Exit is reached!");
				System.out.println();
				return n;
			}
			
			if(freeNeighbour(n.x+1,n.y)) {
				parts[n.x][n.y]= obstacle;
				Node nextN = new Node(n.x+1,n.y,n);
				queue.add(nextN);
			}
			
			if(freeNeighbour(n.x-1,n.y)) {
				parts[n.x][n.y]=obstacle;
				Node nextN = new Node(n.x-1,n.y,n);
				queue.add(nextN);
			}
			
			if(freeNeighbour(n.x,n.y+1)) {
				parts[n.x][n.y]=obstacle;
				Node nextN = new Node(n.x,n.y+1,n);
				queue.add(nextN);
			}
			
			if(freeNeighbour(n.x,n.y-1)) {
				parts[n.x][n.y]=obstacle;
				Node nextN = new Node(n.x,n.y-1,n);
				queue.add(nextN);
			}
		}
		return null;
		
	}

	 public static boolean freeNeighbour(int x, int y) {
//		 System.out.println("Abfrage: x="+x+", y="+y);
//		 System.out.println("Abfrage: parts.length = "+ parts.length);
		 if(x >= 0 && x < parts.length) {
//			 System.out.println("1. Abfrage true!\n parts["+x+"]].length = "+ parts[x].length);
			 if (y >= 0 && y < parts[x].length) {
//				 System.out.println("2. Abfrage true!\nparts["+x+"]["+y+"]="+parts[x][y]);
				 if  (parts[x][y].equals("0")) {
//					 System.out.println("3. Abfrage true - Fall 0!");
					 return true;
					 }
				 else {
					 if (parts[x][y].equals("3")) {
//						 System.out.println("4. Abfrage true - Fall 3!");
						 return true;
					 }
				 }
			 }
		 }
		 return false;
	    }
//	
	
	
	public static void main(String[] args) {
		loadMaze();
		setStart();
		setEnd();
		
		Node n2= solveMaze(startCol, startRow);
		
		System.out.println("Found (reverse) path:");
		 while(n2.getParent() != null) {
	            System.out.println(n2);
	            n2 = n2.getParent();
	        }
		
	}
}
