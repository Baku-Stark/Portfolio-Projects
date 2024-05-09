package Interface;

import java.awt.*;
import java.io.File;
import java.util.ArrayList;
import javax.swing.*;

public class PanelBody extends JPanel{
	private static final long serialVersionUID = 1L;
	
	int value = 0;
	int value_path = 0;
	
	static ArrayList<String> music_list = new ArrayList<String>();
	static JList<Object> list = new JList<Object>();
	
	JPanel panel_right = new JPanel();
	JPanel panel_left = new JPanel();
	
	File dir = new File("C:\\Users\\" + System.getProperty("user.name") + "\\Music");
	File[] list_folder = dir.listFiles();
	
	File directory = new File("C:\\Users\\" + System.getProperty("user.name") + "\\Music\\muryo_player");
	File[] list_files = directory.listFiles();
	
	String USER_COMPUTER(){
		return System.getProperty("user.name");
	}
	
	String OPERATIONAL_SYSTEM() {
		return System.getProperty("os.name");
	}
	
	boolean CHECK_FOLDER() {
		
		if(directory.exists()){
			// CHECK THE FOLDER "muryou_player"
		}
		else {
			// CREATE THE FOLDER "muryou_player"
			directory.mkdir();
			System.out.println("[-] -> FOLDER CREATED!" + "\n");
		}
		
		return true;
	}
	
	

	PanelBody(){
		if(CHECK_FOLDER()) {
			this.setBackground(new Color(47, 47, 47));
			this.setPreferredSize(new Dimension(100, 105));
			this.setOpaque(true);
			
			this.setLayout(new BorderLayout(5, 5));
			
			//for (int i = 0; i < list_files.length; i++) {
			//	if (list_files[i].isFile()) {
			//	    System.out.println(list_files[i].getName());
			//	  }
			//	else if (list_files[i].isDirectory()) {
			//	    System.out.println("Directory " + list_files[i].getName());
			//	  }
			//}
			
			value = list_files.length;
			value_path = list_folder.length;
			
			// ==================== PANEL RIGHT ====================
			panel_right.setBackground(new Color(17, 17, 17));
			panel_right.setPreferredSize(new Dimension(220, 50));
			panel_right.setLayout(new GridLayout(2, 1, 2, 10));
					
			JPanel top_panel = new JPanel();
			top_panel.setBackground(new Color(17, 17, 17));
			top_panel.setLayout(null);
					
			JLabel os_icon = new JLabel();
			os_icon.setBounds(0, 0, 25, 25);
			os_icon.setIcon(new ImageIcon("src/Interface/images/os_icons/"+ OPERATIONAL_SYSTEM() +".png"));
			os_icon.setBackground(new Color(17, 17, 17));
			os_icon.setOpaque(true);
					
			top_panel.add(os_icon);
			top_panel.setOpaque(true);
					
			JPanel bot_panel = new JPanel();
			bot_panel.setBackground(new Color(17, 17, 17));
			bot_panel.setLayout(new BorderLayout());
					
			JPanel container_path = new JPanel();
			container_path.setLayout(new GridLayout(value_path, 1, 15, 15));
			container_path.setBackground(new Color(17, 17, 17));
					
			for (int i = 0; i < value_path; i++) {
				switch (list_folder[i].getName()) {
					case "muryo_player": {
						JPanel path_block = new JPanel();
						path_block.setBackground(new Color(47, 47, 47));
								
						GridBagConstraints c = new GridBagConstraints();
								
						GridBagConstraints c_info = new GridBagConstraints();
						path_block.setLayout(new GridBagLayout());
								
						JButton path = new JButton(list_folder[i].getName());
						path.setBackground(new Color(47, 47, 47));
						path.setForeground(new Color(0xf0f8ff));
						path.setFont(new Font("MV Boli", Font.PLAIN, 15));
						path.setHorizontalTextPosition(JButton.RIGHT);
						path.setBorderPainted(false);
						path.setHorizontalAlignment(SwingConstants.LEFT);
						path.setOpaque(true);
								
						JLabel icon = new JLabel();
						icon.setBounds(1, 1, 1, 1);
						icon.setHorizontalAlignment(JLabel.CENTER);
						icon.setBackground(new Color(47, 47, 47));
						icon.setIcon(new ImageIcon("src/Interface/images//buttons/notes.png"));
						icon.setOpaque(true);
								
						path_block.add(icon, c);
						path_block.add(path, c_info);
						container_path.add(path_block);
					}
					
					default:
						continue;
				}
			}
					
			JScrollPane main_path_list = new JScrollPane(container_path);
			main_path_list.setPreferredSize(new Dimension(220, 1));
			main_path_list.setVerticalScrollBar(new JScrollBar());
					
			bot_panel.add(main_path_list, BorderLayout.WEST);
					
			panel_right.add(top_panel);
			panel_right.add(bot_panel);
			
			// ==================== PANEL LEFT ====================
			this.panel_left.setBackground(new Color(17, 17, 17));
			this.panel_left.setPreferredSize(new Dimension(804, 50));
			panel_left.setLayout(new BorderLayout(5, 5));
			
			JPanel container = new JPanel();
			container.setLayout(new BorderLayout(5, 5));
			container.setBackground(new Color(17, 17, 17));
			
			for (int i = 0; i < value; i++) {
				// ===== SET SONGS IN THE ARRAY
				music_list.add(list_files[i].getName());
			}
			
			//create list)
			list = new JList<Object>(music_list.toArray(new String[music_list.size()]));
			list.setPreferredSize(new Dimension(802, 1));
			list.setFont(new Font("MV Boli", Font.PLAIN, 15));
			list.setForeground(new Color(0xf0f8ff));
			list.setBackground(new Color(17, 17, 17));
			
			container.setPreferredSize(new Dimension(802, 1));
			container.add(list, BorderLayout.WEST);

			panel_left.add(container, BorderLayout.WEST);
			
			// -----
			this.add(panel_right, BorderLayout.WEST);
			this.add(panel_left, BorderLayout.EAST);
		}
		
	}
}