package Interface;

import java.awt.*;
import javax.swing.*;

public class Base extends JFrame{
	/**
	 * Main interface (Layout and Inputs)
	 */
	private static final long serialVersionUID = 1L;
	
	Image icon = Toolkit.getDefaultToolkit().getImage("src/Interface/images/buttons/icon.png");
	
	public Base(){
		this.setTitle("Project Music Player - Java");
	    this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	    this.setSize(1050, 600);
	    this.setResizable(false);
	    this.getContentPane().setBackground(new Color(47, 47, 47));
	    
	    this.setLayout(new BorderLayout(10, 10));
	    this.add(new PanelHeader(), BorderLayout.NORTH);
	    this.add(new PanelBody(), BorderLayout.CENTER);
	    this.add(new PanelFooter(), BorderLayout.SOUTH);
	    
	    this.setIconImage(icon);
	    this.setVisible(true);
	}
}