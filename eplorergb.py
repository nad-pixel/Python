import matplotlib.pyplot as plt

def plot_rgb_color(r, g, b, plot_size=1):
    color = [r / 255.0, g / 255.0, b / 255.0]  # Normalize RGB values to the range [0, 1]
   
    # Set the figure size based on the plot size
    fig, ax = plt.subplots(figsize=(plot_size, plot_size))
    
    ax.imshow([[color]])
    ax.axis('off')
    plt.show()

def explore_rgb_colors(plot_size=0.5):
    for r in range(0, 256, 128):
        for g in range(0, 256, 128):
            for b in range(0, 256, 60):
                plot_rgb_color(r, g, b, plot_size)
                print('#',r,g,b)
              

if __name__ == "__main__":
    explore_rgb_colors(plot_size=2.5)  # Change the plot_size parameter as needed
