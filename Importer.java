import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

import org.neo4j.graphdb.GraphDatabaseService;
import org.neo4j.graphdb.Node;
import org.neo4j.graphdb.Relationship;
import org.neo4j.graphdb.RelationshipType;
import org.neo4j.graphdb.Transaction;
import org.neo4j.graphdb.factory.GraphDatabaseFactory;
import org.neo4j.graphdb.index.Index;
import org.neo4j.graphdb.index.IndexHits;

public class Importer {

	private static enum RelTypes implements RelationshipType {
	    DISLIKES, FRIEND_OF, KNOWS, MARRIED_TO, HAS_DATED
	}
	
	public static void main(String args[]) {
		BufferedReader br = null;
		 
		try {
 
			GraphDatabaseService graphDb;
			//Node firstNode;
			//Node secondNode;
			Relationship relationship;
			
			System.out.println("Starting database...");
			
			graphDb = new GraphDatabaseFactory().newEmbeddedDatabase("/home/velizar/Code/neo4j-community-1.9.4/data/graph.db");
			
			System.out.println("Database started");
			
			String sCurrentLine;

			br = new BufferedReader(new FileReader("output2.txt"));
			Scanner lineScanner;
			long id, target;
			Node nS, nT;
			String rship;
			RelationshipType rType;

			Index<Node> nodeIndex = graphDb.index().forNodes("id");
			IndexHits<Node> nodes;
			Node currentN;
			Transaction tx;
			
			// read line and insert as node
			while ((sCurrentLine = br.readLine()) != null) {
				lineScanner = new Scanner(sCurrentLine);
				id = Long.parseLong(lineScanner.next());
				rship = lineScanner.next();
				target = Long.parseLong(lineScanner.next());
				
				tx = graphDb.beginTx();
				try{
				    // Updating operations go here
					nodes = nodeIndex.get("id", id);
					if(!nodes.hasNext()) {
						// create node
						nS = graphDb.createNode();
						nS.setProperty("id", id);
						nodeIndex.add(nS, "id", id);
					}
					else {
						nS = nodes.next();
					}
					nodes = nodeIndex.get("id", target);
					if(!nodes.hasNext()) {
						nT = graphDb.createNode();
						nT.setProperty("id", target);
						nodeIndex.add(nT, "id", target);
					}
					else {
						nT = nodes.next();
					}
					
					if(rship.equals("DISLIKES"))
						relationship = nS.createRelationshipTo( nT, RelTypes.DISLIKES );
					else if(rship.equals("FRIEND_OF"))
						relationship = nS.createRelationshipTo( nT, RelTypes.FRIEND_OF );
					else if(rship.equals("KNOWS"))
						relationship = nS.createRelationshipTo( nT, RelTypes.KNOWS );
					else if(rship.equals("MARRIED_TO"))
						relationship = nS.createRelationshipTo( nT, RelTypes.MARRIED_TO );
					else if(rship.equals("HAS_DATED"))
						relationship = nS.createRelationshipTo( nT, RelTypes.HAS_DATED );
				    tx.success();
				    
				    System.out.println("Transaction completed.");
				}
				finally{
				    tx.finish();
				}
			}
			
			System.out.println("Done. Shutting down...");
			
			graphDb.shutdown();
 
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)br.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
	
}