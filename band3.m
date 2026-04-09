%% 3D Band Structure Visualization with Three Orientations
clc;
clear;
close all;

% ========== Load Data ==========
kx_mesh = load('KX.grd');      
ky_mesh = load('KY.grd');   
CBM_mesh = load('BAND_LUMO.grd');         
VBM_mesh = load('BAND_HOMO.grd');

% ========== Figure Setup ==========
figure('Color','w','Position',[100, 100, 1200, 400]); % wide figure for 3 subplots
colormap turbo;   % attractive colormap
z_limits = [-2, 2];  % adjust according to your data

% ==================== First Subplot ====================
ax0 = subplot(1,3,1);
surf(kx_mesh, ky_mesh, VBM_mesh, 'FaceAlpha',0.7, 'EdgeColor','none');
hold on;
surf(kx_mesh, ky_mesh, CBM_mesh, 'FaceAlpha',0.7, 'EdgeColor','none');

% Contour projection on z = z_limits(1)
contourf(kx_mesh, ky_mesh, CBM_mesh, 10, 'LineStyle','none');
view(ax0, 0, 0);  % elevation, azimuth
axis tight; axis vis3d;
zlim(z_limits);
shading interp;
grid on;
xlabel('$\it{k}_{x}$','Interpreter','latex','FontName','TimesNewRoman','FontSize',12);
ylabel('$\it{k}_{y}$','Interpreter','latex','FontName','TimesNewRoman','FontSize',12);
zlabel('Energy (eV)','FontSize',12);
set(gca,'FontSize',9);

% ==================== Second Subplot ====================
ax1 = subplot(1,3,2);
surf(kx_mesh, ky_mesh, VBM_mesh, 'FaceAlpha',0.7, 'EdgeColor','none');
hold on;
surf(kx_mesh, ky_mesh, CBM_mesh, 'FaceAlpha',0.7, 'EdgeColor','none');
contourf(kx_mesh, ky_mesh, CBM_mesh, 10, 'LineStyle','none');
view(ax1, 45, 0);  % elevation, azimuth
axis tight; axis vis3d;
zlim(z_limits);
shading interp;
grid on;
xlabel('$\it{k}_{x}$','Interpreter','latex','FontName','TimesNewRoman','FontSize',12);
ylabel('$\it{k}_{y}$','Interpreter','latex','FontName','TimesNewRoman','FontSize',12);
zlabel('Energy (eV)','FontSize',12);
set(gca,'FontSize',9);

% ==================== Third Subplot ====================
ax2 = subplot(1,3,3);
surf(kx_mesh, ky_mesh, VBM_mesh, 'FaceAlpha',0.7, 'EdgeColor','none');
hold on;
surf(kx_mesh, ky_mesh, CBM_mesh, 'FaceAlpha',0.7, 'EdgeColor','none');
contourf(kx_mesh, ky_mesh, CBM_mesh, 10, 'LineStyle','none');
view(ax2, 45, 20);  % elevation, azimuth
axis tight; axis vis3d;
zlim(z_limits);
shading interp;
grid on;
xlabel('$\it{k}_{x}$','Interpreter','latex','FontName','TimesNewRoman','FontSize',12);
ylabel('$\it{k}_{y}$','Interpreter','latex','FontName','TimesNewRoman','FontSize',12);
zlabel('Energy (eV)','FontSize',12);
set(gca,'FontSize',9);

% ==================== Save Figure ====================
set(gcf,'Color','w');
saveas(gcf,'3D_band_structure_three_views.png');

