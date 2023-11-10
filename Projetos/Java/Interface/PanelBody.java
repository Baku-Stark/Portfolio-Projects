package Interface;

import java.awt.*;

import javax.swing.*;

public class PanelBody extends JPanel{
	private static final long serialVersionUID = 1L;
	
	int value = 21;
	JPanel panel_right = new JPanel();
	JPanel panel_left = new JPanel();

	PanelBody(){
		this.setBackground(new Color(47, 47, 47));
		this.setPreferredSize(new Dimension(100, 105));
		this.setOpaque(true);
		
		this.setLayout(new BorderLayout(5, 5));
		// -----
		this.panel_right.setBackground(new Color(17, 17, 17));
		this.panel_right.setPreferredSize(new Dimension(220, 50));
		
		this.panel_left.setBackground(new Color(17, 17, 17));
		this.panel_left.setPreferredSize(new Dimension(804, 50));
		panel_left.setLayout(new BorderLayout(5, 5));
		
		JPanel container = new JPanel();
		container.setLayout(new GridLayout(value, 1, 15, 15));
		container.setBackground(new Color(17, 17, 17));
		
		for (int i = 0; i < value; i++) {
			JPanel song_block = new JPanel();
			song_block.setBackground(new Color(47, 47, 47));
			
			GridBagConstraints c = new GridBagConstraints();
			c.fill = GridBagConstraints.HORIZONTAL;
			c.weightx = 0.8;
			c.gridx = 0;
			c.gridy = 0;
			
			GridBagConstraints c_info = new GridBagConstraints();
			c_info.fill = GridBagConstraints.HORIZONTAL;
			c_info.weightx = 10;
			c_info.gridx = 1;
			c_info.gridy = 0;
			song_block.setLayout(new GridBagLayout());
			
			JButton song = new JButton("Label: " + i);
			song.setBackground(new Color(47, 47, 47));
			song.setForeground(new Color(0xf0f8ff));
			song.setFont(new Font("MV Boli", Font.PLAIN, 15));
			song.setHorizontalTextPosition(JButton.RIGHT);
			song.setBorderPainted(false);
			song.setHorizontalAlignment(SwingConstants.LEFT);
			song.setOpaque(true);
			
			JLabel icon = new JLabel();
			icon.setBounds(1, 1, 1, 1);
			icon.setHorizontalAlignment(JLabel.CENTER);
			icon.setBackground(new Color(47, 47, 47));
			icon.setIcon(new ImageIcon("src/Interface/buttons/notes.png"));
			icon.setOpaque(true);
			
			song_block.add(icon, c);
			song_block.add(song, c_info);
			container.add(song_block);
		}
		
		JScrollPane song_list = new JScrollPane(container);
		song_list.setPreferredSize(new Dimension(802, 1));
		song_list.setVerticalScrollBar(new JScrollBar());

		panel_left.add(song_list, BorderLayout.WEST);
		// -----
		this.add(panel_right, BorderLayout.WEST);
		this.add(panel_left, BorderLayout.EAST);
	}
}