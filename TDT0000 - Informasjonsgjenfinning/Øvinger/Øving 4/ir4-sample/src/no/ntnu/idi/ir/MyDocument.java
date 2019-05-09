package no.ntnu.idi.ir;


import java.io.File;
import java.io.FileNotFoundException;
import org.apache.lucene.document.*;
import org.apache.lucene.index.IndexableField;




public class MyDocument{

    public static Document Document (File f) throws java.io.FileNotFoundException{

        // make a new, empty document
        Document doc = new Document();

        // use the news document wrapper
        NewsDocument newsDocument = new NewsDocument(f);

        //TODO: create structured lucene document
        doc.add(new StringField("id", newsDocument.getId(), Field.Store.YES));
        doc.add(new TextField("from", newsDocument.getFrom(), Field.Store.YES));
        doc.add(new TextField("subject", newsDocument.getSubject(), Field.Store.YES));
        doc.add(new TextField("contents", newsDocument.getContent(), Field.Store.YES));

        return doc;
    }

}