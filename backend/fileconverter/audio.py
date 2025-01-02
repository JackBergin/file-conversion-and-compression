"""
Audio format conversion utilities
"""
from pathlib import Path
from typing import Optional, Union, Literal
from pydub import AudioSegment

class AudioConverter:
    """Handles conversion between different audio formats"""
    
    @staticmethod
    def wav_to_mp3(
        input_file: Union[str, Path],
        output_file: Optional[Union[str, Path]] = None,
        bitrate: str = "192k"
    ) -> Path:
        """
        Convert WAV to MP3 format
        
        Args:
            input_file: Path to input WAV file
            output_file: Optional output MP3 file path
            bitrate: Target bitrate for MP3
            
        Returns:
            Path to created MP3 file
        """
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        if output_file is None:
            output_file = input_path.with_suffix('.mp3')
            
        audio = AudioSegment.from_wav(str(input_path))
        audio.export(str(output_file), format="mp3", bitrate=bitrate)
        
        return Path(output_file)

    @staticmethod
    def wav_to_ogg(
        input_file: Union[str, Path],
        output_file: Optional[Union[str, Path]] = None,
        quality: float = 0.5
    ) -> Path:
        """
        Convert WAV to OGG format
        
        Args:
            input_file: Path to input WAV file
            output_file: Optional output OGG file path
            quality: OGG quality (0.0 to 1.0)
            
        Returns:
            Path to created OGG file
        """
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        if output_file is None:
            output_file = input_path.with_suffix('.ogg')
            
        audio = AudioSegment.from_wav(str(input_path))
        audio.export(str(output_file), format="ogg", parameters=["-q", str(quality)])
        
        return Path(output_file) 