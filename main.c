#include <stdio.h>
#include <linux/videodev2.h>

int main() {
    const int resolutions[][2] = {{640, 1480}, {1024, 768}, {1920, 1040}, {2920, 1040}};

    int num_photos;
    int delay;
    int res_pick;
    int chosen_res[2];

    printf("Choose the number of photos: ");
    scanf("%d", &num_photos);

    printf("Choose the delay between captures (seconds): ");
    scanf("%d", &delay);
    
    printf("1. %dx%d\n2. %dx%d\n3. %dx%d\n", resolutions[0][0], resolutions[0][1], resolutions[1][0], resolutions[1][1], resolutions[2][0], resolutions[2][1]);

    printf("Select the resolution (1, 2 or 3): ");
    scanf("%d", &res_pick);

    chosen_res[0] = resolutions[res_pick][0];
    chosen_res[1] = resolutions[res_pick][1];

    printf("You have opted to take %d photos with a %dx%d resolution and a %d second delay between each take.\n", num_photos, chosen_res[0], chosen_res[1], delay);
}