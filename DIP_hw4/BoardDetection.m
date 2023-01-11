
% The runtime of the script is about 1min

img_model = imread('.\image\template.png');
img_model = rgb2gray(img_model);

% template bounding box area
template_bounding_box = [34, 69; 464, 70; 486, 324; 12, 322; 34, 69];

% apply KAZE on template image
pts_model = detectKAZEFeatures(img_model).selectStrongest(2000);
[features_model, pts_model] = extractFeatures(img_model, pts_model);

for i = 1:13

    img_path = sprintf('%s%d%s', '.\image\', i, '.png')
    img_detect_rgb = imread(img_path);
    img_detect = rgb2gray(img_detect_rgb);
    
    % apply KAZE on test image
    pts_detect = detectKAZEFeatures(img_detect);
    [features_detect, pts_detect] = extractFeatures(img_detect, pts_detect);
    
    % match the feature points
    idx_match = matchFeatures(features_model, features_detect, ...
        'MatchThreshold', 10, 'MaxRatio', 0.5);
    
    % match points extraction
    pts_match_model = pts_model(idx_match(:, 1), :);
    pts_match_detect = pts_detect(idx_match(:, 2), :);
    
    % MASC
    [tform, ~] = estimateGeometricTransform2D(pts_match_model, pts_match_detect, 'affine');
    
    % Transform the template bounding box
    test_bounding_box = transformPointsForward(tform, template_bounding_box);
    
    % save to ./result
    save_path = sprintf('%s%d%s', '.\result\', i, '.png');
    figure('Visible','off');
    imshow(img_detect_rgb);
    hold on;
    line(test_bounding_box(:, 1), test_bounding_box(:, 2), 'Color', 'y', 'LineWidth', 2 );
    hold off;
    frame = getframe;
    im = frame.cdata;
    imwrite(im, save_path); 

end
