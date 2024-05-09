package Functions;

import java.io.File;
import java.io.IOException;

import javax.sound.sampled.*;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

public class Song_Functions{
	static String music_folder = "";
	
	static AudioInputStream audioStream;
	static Clip clip;
	
	public static void Play_Song(String song, String response)  throws LineUnavailableException, UnsupportedAudioFileException, IOException{
		//System.out.println("Playing: " + song);
		music_folder = "C:\\Users\\" + System.getProperty("user.name") + "\\Music\\muryo_player\\" + song;
		audioStream = AudioSystem.getAudioInputStream(new File(music_folder));
		
		
		
		if(music_folder.length() > 0 && response == "play") {
			clip = AudioSystem.getClip();
			clip.open(audioStream);
			clip.start();
		}
		
		else {
			clip = AudioSystem.getClip();
			clip.open(audioStream);
			clip.close();
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