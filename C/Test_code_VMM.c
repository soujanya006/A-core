#include <stdio.h>
#include "vmm_utils.h"
#include "a-core-utils.h"
#include "print_float.h"
#include "image.h"


static const float filter[3][3] = {
        {1, 0, -1},
        {1, 0, -1},
        {1, 0, -1}
};


void main() {
        //These for the first example of just printing first element of image and filter data
        // print_float(image[0][0]);
        // print_float(filter[0][0]);

        for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                        vmm_write_vec_in_float(3*i + j, image[i][j]);
                        // print_float(image[i][j]);
                        // printf("\n");
                }
        }

        for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                        vmm_write_mat_in_float(3*i + j, 0, filter[i][j]);
                        vmm_write_mat_in_float(3*i + j + 3, 1, filter[i][j]);
                        vmm_write_mat_in_float(3*i + j + 6, 2, filter[i][j]);
                        vmm_write_mat_in_float(3*i + j + 9, 3, filter[i][j]);
                }
        }

        float result = vmm_read_vec_out_float(0);
        float result = vmm_read_vec_out_float(1);
        float result = vmm_read_vec_out_float(2);
        float result = vmm_read_vec_out_float(3);

        print_float(result);
        printf("\n");

        vmm_write_sram_rd(1);

        test_pass();
}
