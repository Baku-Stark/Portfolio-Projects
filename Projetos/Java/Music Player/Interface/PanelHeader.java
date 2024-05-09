package Interface;

import java.awt.*;
import javax.swing.*;

public class PanelHeader extends JPanel{
	private static final long serialVersionUID = 1L;
	
	JPanel title_box = new JPanel();
	JLabel title = new JLabel("Muryo Player");

	PanelHeader(){
		this.setBackground(new Color(17, 17, 17));
		this.setPreferredSize(new Dimension(100, 50));
		this.setOpaque(true);
		this.setLayout(new BorderLayout());
		// -----
		title.setVerticalAlignment(JLabel.CENTER);
        title.setHorizontalAlignment(JLabel.CENTER);
		title.setForeground(new Color(0xf0f8ff));
		title.setBackground(new Color(17, 17, 17));
		title.setFont(new Font("MV Boli", Font.PLAIN, 25));
		title.setOpaque(true);
		
		title_box.add(title);
		title_box.setBackground(new Color(17, 17, 17));
		// -----
		
		this.add(title_box, BorderLayout.CENTER);
		
	}
}