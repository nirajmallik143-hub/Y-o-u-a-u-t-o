import os
from script_gen import generate_kids_script
from image_gen import generate_auto_image
from video_gen import build_kids_video

def run_fully_automated_pipeline():
    print("Starting Fully Automated Pipeline (Script -> Voice -> Auto-Image -> Video)...")
    
    # 1. Generate 2 Shorts (1 minute each)
    for i in range(1, 3):
        print(f"\n--- Processing Short #{i} ---")
        script = generate_kids_script("short")
        
        # Auto-generate high-quality picture for this short
        image_path = generate_auto_image(f"Yummy Short #{i}", f"assets/short_scene_{i}.jpg", is_short=True)
        
        # Build final video (Short = 60 seconds)
        output_name = f"short_{i}.mp4"
        build_kids_video(script, image_path, output_name, duration_seconds=60)

    # 2. Generate 1 Long Video (5 minutes)
    print("\n--- Processing Long Video (5 min) ---")
    long_script = generate_kids_script("long")
    
    # Auto-generate high-quality picture for the long video
    long_image_path = generate_auto_image("Yummy Story Adventure", "assets/long_scene.jpg", is_short=False)
    
    long_output = "long_video_1.mp4"
    build_kids_video(long_script, long_image_path, long_output, duration_seconds=300)

    print("\nAll 2 Shorts and 1 Long video successfully built automatically!")

if __name__ == "__main__":
    run_fully_automated_pipeline()
