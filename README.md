# Streamline-Based Analysis User Guide
This document provides a user guide to conduct Streamline-Based Analysis (SBA) as presented in [Preprint/Paper].

## 1. Pre-processing
The desirable pre-processing steps will vary depending on the specific dataset. Please, refer to external resources, such as this [tutorial](https://andysbrainbook.readthedocs.io/en/latest/MRtrix/MRtrix_Course/MRtrix_04_Preprocessing.html) or this [tutorial](https://mrtrix.readthedocs.io/en/dev/fixel_based_analysis/mt_fibre_density_cross-section.html) up to step 8.

## 2. Template construction
The specific strategy used to construct the template tractogram for the presented aplication closesy follows what described in a previous [tutorial](https://github.com/Jinglei-Lv/Tissue_Unbiased_FOD_Tractogram_Template). An exception is made for the "fibre tracking" step.

In this case, we proposed the following approach:
- **Raw tractogram generation**: this step yields a 1M template tractogram
```bash
tckgen FOD_template.mif.gz tracks_raw_template.tck -angle 22.5 -power 1.0 -select 1M -seed_dynamic FOD_template.mif.gz -act 5tt_template.mif -backtrack -minlength 10 -maxlength 250 -max_attempts_per_seed 1000 
```
- **Template tractogram filtering**: this step allows filtering the template tractogram to reduce streamline redundancy
```bash
tcksift tracks_raw_template.tck FOD_template.mif.gz tracks_filtered_template.tck 
```
- **Further filtering**: at this stage the user may decide to implement further filtering according to criteria of choice (e.g. required WM intersection in each subject space)

## 3. Template tractogram refinement
To minimise erroneous streamline sampling in subject space, SBA offers a back-tracking/re-tracking tool for tractograms warped to subject space. Please, refer to available community forum [resources](https://community.mrtrix.org/t/registration-using-transformations-generated-from-other-packages/2259) regarding tractograms registration.
```bash
tckbacktrack tracks_filtered_template_subjectspace.tck FOD_subject.mif.gz 5tt_subjectspace.mif.gz tracks_filtered_template_subjectspace_refined.tck 
```
<p align="center">
  <img src="figures/tracks_refinement_github.jpg" width="70%">
</p>

<p align="center">
  <em>
    Qualitative comparison between template streamlines projected to subject space (“raw”) and their “refined” back-tracking/re-tracking version in four magnified regions from a slice of a representative subject. Streamlines are overlaid on tissue segmentation to provide high anatomical contrast (Cerebro Spinal Fluid – CSF; cortical Gray Matter – cGM; White Matter - WM). The refinement effect of this procedure can be observed in the improvements of regions with lack of WM coverage, and elimination of spurious cGM and CSF incursions.
  </em>
</p>


