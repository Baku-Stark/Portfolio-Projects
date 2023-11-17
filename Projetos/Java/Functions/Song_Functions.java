package Functions;

import java.io.File;
import java.io.IOException;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

public class Song_Functions{
	
	public static void Play_Song(String song, boolean response)  throws LineUnavailableException, UnsupportedAudioFileException, IOException{
		//System.out.println("Playing: " + song);
        
        AudioInputStream audioStream = AudioSystem.getAudioInputStream(new File("C:\\Users\\" + System.getProperty("user.name") + "\\Music\\muryo_player\\" + song));
        
        Clip clip = AudioSystem.getClip();
        clip.open(audioStream);
        
        if(response) {
        	clip.start();
        }
        
        else {
        	clip.stop();
        }
	}
	
	public static void Prev_Song(){
		System.out.println("Hello - Previous");
	}
	
	public static void Next_Song(){
		System.out.println("Hello - Next");
	}
	
	public static void Repeat_Song(boolean sit){
		if(sit) {
			System.out.println("Hello - Repeat");
		}
		
		else {
			System.out.println("Hello - NO_Repeat");
		}
	}
	
	public static void Shuffle_Song(boolean sit){
		if(sit) {
			System.out.println("Hello - Shuffle");
		}
		
		else {
			System.out.println("Hello - NO_Shuffle");
		}
	}
}